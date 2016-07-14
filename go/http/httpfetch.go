package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

type Cell_JS struct {
	fund_id             string
	fund_nm             string
	asset_ratio         string
	price               string
	price_dt            string
	increase_rt         string
	volume              string
	stock_volume        string
	last_time           string
	amount              string
	amount_incr         string
	amount_increase_rt  string
	fund_nav            string
	nav_dt              string
	estimate_value      string
	last_est_time       string
	discount_rt         string
	index_id            string
	index_nm            string
	index_increase_rt   string
	apply_fee           string
	apply_fee_tips      string
	redeem_fee          string
	redeem_fee_tips     string
	apply_status        string
	redeem_status       string
	min_amt             string
	notes               string
	apply_redeem_status string
	amount_incr_tips    string
	turnover_rt         string
}

type Row_JS struct {
	Id   string
	Cell map[string]string
}

type Lof_JS struct {
	Page int
	Rows []Row_JS
}

func main() {
	res, err := http.Get("http://www.jisilu.cn/data/lof/index_lof_list/?___t=1459354520266")

	if err != nil {
		log.Fatal(err)
	}
	robots, err := ioutil.ReadAll(res.Body)
	res.Body.Close()
	if err != nil {
		log.Fatal(err)
	}
	var f interface{}

	err = json.Unmarshal(robots, &f)

	if err != nil {
		fmt.Println("error:", err)
	}

	m := f.(map[string]interface{})

	for k, v := range m {
		switch vv := v.(type) {
		case string:
			fmt.Println(k, "is string", vv)
		case int:
			fmt.Println(k, "is int", vv)

		case []interface{}:

			fmt.Println(k, "is an array:")
			for i, u := range vv {
				//fmt.Println(i, u)
				//strs := u["id"].([]interface{})
				//str1 := strs[0].(string)
				//fmt.Println(str1)
				i = i

				my := u.(map[string]interface{})
				strs := my["id"].(interface{})
				str1 := strs.(string)
				fmt.Print(str1)

				cell := my["cell"].(map[string]interface{})

				appfees := cell["apply_fee"].(string)
				fmt.Print(appfees)
			}
		default:
			fmt.Println(k, "is of a type I don’t know how to handle")
		}
	}
}
