package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var lines []string

func GetLines(fname string) (lines []string) {
	f, err := os.Open(fname)
	if err != nil {
		panic(err)
	}
	defer f.Close()
	s := bufio.NewScanner(f)
	for s.Scan() {
		lines = append(lines, s.Text())
	}
	if s.Err() != nil {
		panic(s.Err)
	}
	return
}

func p1() {
	calPerElf := []int{0}
	max := 0
	for _, line := range lines {
		if len(line) == 0 {
			calPerElf = append(calPerElf, 0)
			continue
		}
		tmp, err := strconv.Atoi(line)
		if err != nil {
			panic(err)
		}
		calPerElf[len(calPerElf)-1] += tmp
		if calPerElf[len(calPerElf)-1] > max {
			max = calPerElf[len(calPerElf)-1]
		}
	}
	fmt.Println(max)
}

func p2() {
	calPerElf := []int{0}
	for _, line := range lines {
		if len(line) == 0 {
			calPerElf = append(calPerElf, 0)
			continue
		}
		tmp, err := strconv.Atoi(line)
		if err != nil {
			panic(err)
		}
		calPerElf[len(calPerElf)-1] += tmp
	}
	res := 0
	for i := 0; i < 3; i++ {
		max := 0
		maxIdx := 0
		for j, cals := range calPerElf {
			if cals > max {
				max = cals
				maxIdx = j
			}
		}
		res += max
		calPerElf[maxIdx] = calPerElf[len(calPerElf)-1]
		calPerElf = calPerElf[:len(calPerElf)-1]
	}
	fmt.Println(res)
}

func main() {
	lines = GetLines("01.txt")
	p1()
	p2()
}
