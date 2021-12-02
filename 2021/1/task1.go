package main

import (
    "fmt"
    "io/ioutil"
    s "strings"
    "strconv"
)

func main() {
    data, err := ioutil.ReadFile("input.txt")
    if err != nil {
        fmt.Println("Error opening file")
        return
    }
    str := s.Trim(s.Replace(string(data), "\r", "", -1), "\n")
    list := s.Split(str, "\n")
    last := 0
    count := 0
    for i, line := range list {
        val, err := strconv.Atoi(line)
        if err != nil {
            fmt.Println("Error converting string to number: ", line)
        }
        if (i > 0 && last < val) {count += 1 }
        last = val
    }
    fmt.Println(count)
}
