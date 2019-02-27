use log::*;
use std::fmt::Display;
use std::process::{Command, Output};

struct StrOutput(std::process::Output);

fn main() {
    env_logger::init();

    println!("Hello, world!");

    let initial_branch_name = get_current_branch_name();

    println!("Switching to master...");
    checkout("master");

    println!("Doing some calculation right now");

    println!("... and back to {}", &initial_branch_name);
    checkout(&initial_branch_name.to_string());
}

impl Display for StrOutput {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "{}", String::from_utf8_lossy(&self.0.stdout).trim())
    }
}

fn checkout(target_branch: &str) {
    let checkout = Command::new("git")
        .arg("checkout")
        .arg(target_branch)
        .output()
        .expect("Failed to execute command");
    report(&checkout);
}

fn get_current_branch_name() -> StrOutput {
    let br_name_command = Command::new("git")
        .arg("rev-parse")
        .arg("--abbrev-ref")
        .arg("HEAD")
        .output()
        .expect("Failed to get branch name");
    report(&br_name_command);
    StrOutput(br_name_command)
}

fn report(output: &Output) {
    let stdout = String::from_utf8_lossy(&output.stdout);
    if !stdout.is_empty() {
        info!("stdout: {}", stdout);
    }

    let stderr = String::from_utf8_lossy(&output.stderr);
    if !stderr.is_empty() {
        if output.status.success() {
            info!("stderr: {}", stderr);
        } else {
            error!("stderr: {}", stderr);
        }
    }
}
