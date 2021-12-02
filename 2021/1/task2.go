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
    AVGLEN := 3
    ring := make([]int, AVGLEN)
    for i := 1; i < AVGLEN; i++ {
        ring[i] = 0
    }
    sum := 0
    for i, line := range list {
        val, err := strconv.Atoi(line)
        if err != nil {
            fmt.Println("Error converting string to number: ", line)
        }
        sum -= ring[i % AVGLEN]
        sum += val
        ring[i % AVGLEN] = val
        if (i > 2 && last < sum) {count += 1 }
        last = sum
    }
    fmt.Println(count)
}
