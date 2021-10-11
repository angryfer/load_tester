package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"strconv"
	"sync"
)

func main() {
	argsLength := len(os.Args)

	var host string
	var workers int

	if argsLength > 1 {
		host = os.Args[1]
	} else {
		fmt.Println("Error: No hostname provided. Add hostname as first argument.")
		os.Exit(1)
	}

	if argsLength > 2 {
		wrks, err := strconv.Atoi(os.Args[2])
		workers = wrks
		if err != nil {
			fmt.Println(err)
		}
	} else {
		fmt.Println("Error: No number of workers (threads) provided. Add number of workers as second argument.")
		os.Exit(1)
	}

	var wg sync.WaitGroup

	for i := 0; i < workers; i++ {
		fmt.Println("Starting Worker", i)
		wg.Add(1)
		go worker(&wg, i, host)
		fmt.Println("go")
	}

	fmt.Println("Waiting for Workers to finish")
	wg.Wait()
}

func worker(wg *sync.WaitGroup, id int, host string) {
	// Workers will run forever
	for {
		resp, err := http.Get(host)
		if err != nil {
			fmt.Println(err)
		}

		defer resp.Body.Close()
		body, err := ioutil.ReadAll(resp.Body)

		if err != nil {
			fmt.Println(err)
		}

		fmt.Println(string(body))
	}
}
