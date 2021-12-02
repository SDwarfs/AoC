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


func Atoi(str string) int {
    val, err := strconv.Atoi(str)
    if err != nil {
        fmt.Println("Error converting string to number: ", str)
        os.Exit(2)
    }
    return val
}


func main() {
    list := getFileAsList("input.txt")
    depth := 0
    hpos := 0
    for _, line := range list {
        arr := s.Split(line, " ")
        cmd := arr[0]
        valstr := arr[1]
        val := Atoi(valstr)
        if (cmd == "forward") { hpos += val }
        if (cmd == "up")      { depth -= val }
        if (cmd == "down")    { depth += val }
    }
    fmt.Println("Depth:", depth, ", H-Pos: ", hpos, ", Product: ", depth*hpos)
}
