package main

import (
	"flag"
	"fmt"
	"github.com/olekukonko/tablewriter"
	"io/ioutil"
	"log"
	"os"
	"os/exec"
	"strconv"
	"strings"
	"sync"
)

var wg sync.WaitGroup

const header = "\033[95m"
const blue = "\033[94m"
const green = "\033[92m"
const orange = "\033[93m"
const red = "\033[91m"
const endc = "\033[0m"
const bold = "\033[1m"
const underline = "\033[4m"

type result struct {
	oldScore int
	newScore int
	status   string
}

func makebold(s string) string {
	return bold + s + endc
}
func okgreen(s string) string {
	return green + s + endc
}
func warnorange(s string) string {
	return orange + s + endc
}
func nokred(s string) string {
	return red + s + endc
}
func okblue(s string) string {
	return blue + s + endc
}

func main() {
	datasets := flag.String("datasets", "ABCDE", "datasets to evaluate")
	model := flag.String("model", "./main.sh", "model file")
	scorer := flag.String("scorer", "./scorer.sh", "scorer file")
	datafolder := flag.String("datafolder", "data", "folder containing datasets")

	flag.Parse()

	results := make([]result, len(*datasets))
	for i, c := range *datasets {
		results[i] = result{-1, -1, nokred("worse")}
		wg.Add(1)
		go testDataset(string(c), *model, *scorer, &results[i], *datafolder)
	}
	wg.Wait()

	resTable := tablewriter.NewWriter(os.Stdout)
	resTable.SetHeader([]string{"Test case", "Old score", "New score", "Status"})
	resTable.SetRowLine(true)
	for i, c := range *datasets {
		r := results[i]
		resTable.Append([]string{bold + string(c) + endc, strconv.Itoa(r.oldScore), strconv.Itoa(r.newScore), r.status})
	}
	resTable.Render()
}

func testDataset(c string, model string, scorer string, res *result, datafolder string) {
	defer wg.Done()

	scoreFileName := datafolder + "/" + c + ".score"
	inputFileName := datafolder + "/" + c + ".in"
	outputFileName := datafolder + "/" + c + ".out"
	tmpOutputFileName := datafolder + "/" + c + ".out.tmp"

	tmpOutput, err := exec.Command(model, inputFileName, tmpOutputFileName).CombinedOutput()
	if err != nil {
		fmt.Println("---\nmain output for dataset " + c + ":\n" + string(tmpOutput) + "---")
		log.Println("Error executing model:", err)
		return
	}

	var oldScore int
	{
		tmp, err := ioutil.ReadFile(scoreFileName)
		if err != nil {
			log.Println("Couldn't load ", scoreFileName, ":", err)
			oldScore = 0
		} else {
			oldScore, err = strconv.Atoi(strings.TrimSpace(string(tmp)))
			if err != nil {
				log.Println("Couldn't parse oldScore as int: ", oldScore)
				return
			}
		}
	}

	var newScore int
	{
		tmp, err := exec.Command(scorer, inputFileName, tmpOutputFileName).Output()
		if err != nil {
			log.Println("Error computing new score:", err)
			return
		}

		newScore, err = strconv.Atoi(strings.TrimSpace(string(tmp)))
		if err != nil {
			log.Println("Couldn't parse new score as int: ", oldScore)
			return
		}

		if newScore > oldScore {
			_, err := exec.Command("cp", tmpOutputFileName, outputFileName).CombinedOutput()
			if err != nil {
				log.Println("Failed to override the submission:", err)
				return
			}
			err = ioutil.WriteFile(scoreFileName, tmp, 0777)
			if err != nil {
				log.Println("Error writing new score:", err)
				return
			}
			res.status = okgreen("better")
		} else if newScore == oldScore {
			res.status = warnorange("same")
		}
	}
	res.oldScore = oldScore
	res.newScore = newScore

	modelOutput := okblue(makebold(c+", model output:")) + "\n" + string(tmpOutput)
	fmt.Println(modelOutput + "---")
}
