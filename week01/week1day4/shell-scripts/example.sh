#!/bin/bash                                     
set -euo pipefail                                      #makes script safer

show_help(){                                           #function to display help
    echo "usage: $0 <name>"
    echo "options:"
    echo " -h, --help  show help"
}
greet(){                                                #function to greet user
    local name="$1"
    echo "Hello,$name!"
    }
if [[ $# -eq 0 ]]; then                                 #check if no argument is provided
    echo "Error: Name is required."
    show_help
    exit 1
fi

if [[ "$1" == "-h" || "$1" == "--help" ]]; then         #show help when -h or -help is used
    show_help
    exit 0
fi

greet "$1"                                              #calll the greet function