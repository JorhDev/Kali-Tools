package main

import (
	"fmt"
	"math/rand"
)

func main() {
	mana := 0
	for i := 0; i < 10000000; i++ {
		if mana == rand.Intn(100000) {
			fmt.Println("Выпало число 0")
			break
		} else {
			fmt.Println(i)
		}
	}
}
