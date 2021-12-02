package main

import (
    "fmt"
    "os"
    "io/ioutil"
    s "strings"
    "strconv"
)

func getFileAsList(fn string) []string {
    data, err := ioutil.ReadFile(fn)
    if err != nil {
        fmt.Println("Error opening file")
        os.Exit(1)
    }
    str := s.Trim(s.Replace(string(data), "\r", "", -1), "\n")
    list := s.Split(str, "\n")
    return list
}


func getFileAsIntList(fn string) []int {
    list := getFileAsList(fn)
    intList := make([]int, len(list))
    for i, line := range list {
        val, err := strconv.Atoi(line)
        if err != nil {
            fmt.Println("Error converting string to number: ", line)
            os.Exit(2)
        }
        intList[i] = val
    }
    return intList
}

var AVGLEN int
var ring []int
var index int
var sum int

func initSlidingSum(Len int) {
    AVGLEN = Len
    ring = make([]int, AVGLEN)
    for i := 1; i < AVGLEN; i++ {
        ring[i] = 0
    }
    sum = 0
    index = 0
}

func getSlidingSum(val int) int {
    sum -= ring[index]
    sum += val
    ring[index] = val
    index = (index + 1) % AVGLEN
    return sum
}

func main() {
    list := getFileAsIntList("input.txt")
    initSlidingSum(3)

    last := 0
    count := 0
    for i, v := range list {
        ssum := getSlidingSum(v)
        if (i > (AVGLEN-1) && last < ssum) {count += 1 }
        last = sum
    }
    fmt.Println(count)
}
