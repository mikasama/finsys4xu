<template>
    <div class="city">
        <!-- <h1>{{ name }}</h1> -->
        <button v-on:click="getCity">click it  </button>  
        <el-button type="primary" v-on:click="getCity">click it</el-button>
        <el-table
            :data="tableData"
            stripe
            style="width: 100%">
            
            <el-table-column
                prop="Country"
                label="国家"
                width="180">
            </el-table-column>
            <el-table-column
                prop="CountryPopulation"
                label="人口"
                width="180">
            </el-table-column>
            <el-table-column
                prop="Province"
                label="省份"
                width="180">
            </el-table-column>
            <el-table-column
                prop="CreateAt"
                label="创建时间">
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
    export default {
        name: "city",
        data() {
            return {
                name: 'show city',
                tableData: [
                    
                ]
            }
        },
        methods: {
            getCity() {
                var that = this
                that.loadingStatus = true
                const axios = require('axios')
                var url = 'http://127.0.0.1:8888/api/v1/city'
                console.log(url)
                axios.get(url)
                .then(function (response) {
                    // console.log(response)
                    console.log("response.data:", response.data)  //返回list嵌套字典
                    // that.$set(that.data, "tableData", response.data)
                    // console.log(that.data)
                    that.tableData = response.data  // data（）里面的字段可以直接取，this不行就that
                    that.loadingStatus = false
                    return that.tableData
                })
                .catch(function (error) {
                    console.log(error)
                })
            },

            getCityData() {
                this.getCity
            }
        },
        beforeCreate() {
            console.log("before")
            var that = this
            that.tableData = that.getCity()
            console.log("that.tableData", that.tableData)
            }
    }
</script>

<style>

</style>