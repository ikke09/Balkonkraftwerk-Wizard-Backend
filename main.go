package main

import (
	"github.com/gin-gonic/gin"
	"log"
)

func setupRouter() *gin.Engine {
	r := gin.Default()
	r.GET("/ping", func(c *gin.Context) {
		c.String(200, "pong")
	})
	return r
}

func main() {
	r := setupRouter()
	log.Fatal(r.Run(":8080"))
}
