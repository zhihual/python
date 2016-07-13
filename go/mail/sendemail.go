package main

import (
	"log"
	"net/smtp"
)

func main() {
	send("First Go lange to send one email")
}

func send(body string) {
	from := "dikehua@sina.com"
	pass := "7275337"
	to := "7275337@qq.com"

	msg := "From: " + from + "\n" +
		"To: " + to + "\n" +
		"Subject: Hello there\n\n" +
		body

	err := smtp.SendMail("smtp.sina.cn:587",
		smtp.PlainAuth("", from, pass, "smtp.sina.cn"),
		from, []string{to}, []byte(msg))

	if err != nil {
		log.Printf("smtp error: %s", err)
		return
	}

	log.Print("sent, check Weichat\n")
}
