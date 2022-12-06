package day_04

import "core:strings"
import "core:strconv"
import "core:fmt"
import "core:os"

main :: proc() {
    data, success := os.read_entire_file_from_filename("04.txt")
    if !success {
        fmt.println("Couln't load file at " + "04.txt")
        return
    }
    total_a : int
    total_b : int

    text := string(data)
    lines := strings.split(text, "\r\n")

    for line in lines {
        values := strings.split(line, ",")
        first := strings.split(values[0], "-")
        second := strings.split(values[1], "-")

        x1 := strconv.atoi(first[0])
        y1 := strconv.atoi(first[1])
        x2 := strconv.atoi(second[0])
        y2 := strconv.atoi(second[1])
        
        total_a += int((x1 <= x2 && y1 >= y2) || (x1 >= x2 && y1 <= y2))
        total_b += int(y1 >= x2 && x1 <= y2) 
   }   

   fmt.println(total_a, total_b)
}