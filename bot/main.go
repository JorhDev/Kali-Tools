package main

import "fmt"

func main() {
	//🐤
	//🔋
	score := 0
	score_cell := 1

	for i := 1; i <= 11; i++ {

		fmt.Println("Get Ready")
		fmt.Println("Счет:", score)
		fmt.Println("")

		fmt.Println("Вы подлетаете к трубе!", score_cell)
		fmt.Println("🐤🔋🔋")
		fmt.Println("")

		fmt.Println("Вы пролетаете через трубу!")
		fmt.Println("🔋🐤🔋")
		fmt.Println("")

		fmt.Println("Вы пролетели через трубу!")
		fmt.Println("🔋🔋🐤")
		fmt.Println("")

		score++
		score_cell++

		fmt.Println("Счет:", score)
		fmt.Println("")
	}
}
