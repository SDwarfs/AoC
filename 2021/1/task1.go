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


func main() {
    list := getFileAsIntList("input.txt")
    last := 0
    count := 0
    for i, val := range list {
        if (i > 0 && last < val) {count += 1 }
        last = val
    }
    fmt.Println(count)
}
