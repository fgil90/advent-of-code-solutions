package day_05

import "core:fmt"
import "core:os"
import "core:strings"
import "core:strconv"
import "core:slice"

Columns :: [dynamic][dynamic]u8

main :: proc() {
    data, success := os.read_entire_file_from_filename("05.txt")
    defer delete(data)
    if !success do return 
    text := string(data)
    lines := strings.split(text, "\r\n")
    columns, next_line_idx := parse_columns(lines)

    instructions := lines[next_line_idx:]

    fmt.println(parse_instructions(instructions, columns))
}

parse_columns :: proc(lines: []string) -> (Columns, int){

    max_height : int
    n_cols := (1 + len(lines[0]))/4
    
    for line in lines {
        if len(line) == 0 do break
        max_height += 1
    }    
    max_height -= 1
    
    columns := make(Columns, n_cols)
    
    for line_idx := max_height-1; line_idx >= 0; line_idx -= 1 {
        line := lines[line_idx]

        for ch_idx := 1; ch_idx < len(line); ch_idx += 4 {
            ch := line[ch_idx]
            if ch == ' ' do continue 
            append(&columns[(ch_idx-1)/4], ch)
        }
    }
    return columns, max_height+2
}

parse_instructions :: proc(lines: []string, columns: Columns ) -> string{
    buffer := make([dynamic ]u8, len(columns))
    
    for line in lines{
        line_array := strings.split(line, " ")
        amount := strconv.atoi(line_array[1])
        source := strconv.atoi(line_array[3]) - 1
        target := strconv.atoi(line_array[5]) - 1

        length := len(columns[source])
        stack := columns[source][length-amount:]
        // slice.reverse(stack)
        append(&columns[target], ..stack)
        remove_range(&columns[source], length - amount, length)
    }
    for col, i in columns{
        buffer[i] = col[len(col)-1]
    }

    return string(buffer[:])
}