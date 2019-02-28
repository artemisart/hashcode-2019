#!/bin/sh
go build runner.go
GOOS=windows GOARCH=amd64 go build runner.go
mv runner ..
mv runner.exe ..
