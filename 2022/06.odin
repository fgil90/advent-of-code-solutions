package day_06

import "core:strings"
import "core:os"
import "core:fmt"

main :: proc() {
    data, success := os.read_entire_file_from_filename("06.txt")
    defer delete(data)
    if !success do return 
    text := string(data)
    fmt.println(find_marker(text))

}

find_marker :: proc(text:string) -> int{
    start_loop : for start in 0..<len(text)-13{
        ch_loop : for a in start..<start+13{
            for b in a+1..=start+13{
                if text[a] == text[b] do continue start_loop
            }
        }

        return start+14

        // if  text[start+0] != text[start+1] &&
        //     text[start+0] != text[start+2] &&
        //     text[start+0] != text[start+3] &&
        //     text[start+1] != text[start+2] &&
        //     text[start+1] != text[start+3] &&
        //     text[start+2] != text[start+3] {

        //     return start+4
        // }
    }
    return -1
}