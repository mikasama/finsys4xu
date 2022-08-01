<template>
    <div class="wencai">
        <el-form :inline="true" :model="findFilters" class="inline-form">
            <el-form-item label="股票名称">
                <el-input v-model="findFilters.StockName" placeholder="股票名称"></el-input>
            </el-form-item>
            <el-form-item label="股票代码">
                <el-input v-model="findFilters.StockCode" placeholder="股票代码"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="getDataFromFilter">查询</el-button>
            </el-form-item>
        </el-form>
        <el-button type="primary" v-on:click="getWencaiData">查询</el-button>
        <el-table
            :data="wencaiData"
            stripe
            style="width: 100%">

            <el-table-column
                prop="id"
                label="序号"
                width="100px">
            </el-table-column>
            <el-table-column
                prop="stockname"
                label="股票名称"
                width="180px">
            </el-table-column>
            <el-table-column
                prop="stockcode"
                label="股票代码"
                width="180px">
            </el-table-column>
            <el-table-column
                prop="wencaiscore"
                label="问财评分"
                width="180px">
            </el-table-column>
            <el-table-column
                prop="shortcommnet"
                label="短评"
                width="180px">
            </el-table-column>
            <el-table-column
                prop="langcommnet"
                label="长评"
                width="180px">
            </el-table-column>
            <el-table-column
                prop="morecontent"
                label="更多评论"
                width="250px">
            </el-table-column>
            <el-table-column
                prop="createtime"
                label="创建时间"
                width="180px">
            </el-table-column>
            <el-table-column
                prop="updatetime"
                label="更新时间"
                width="180px">
            </el-table-column>
            <el-table-column
                prop="Options"
                label="操作">
            </el-table-column>

        </el-table>
    </div>
</template>

<script>
    export default {
        name: "wencai",
        data() {
            return {
                wencaiData: [

                ],
                findFilters: {
                    StockName: '',
                    StockCode: ''
                }
            }
        },
        methods: {
            getWencaiData() {
                var that = this
                that.loadingStatus = true
                const axios = require('axios')
                // var url = 'http://127.0.0.1:8888/api/v1/wencai'
                var url = 'http://localhost:9999/financial/get_all_stock'
                axios.get(url)
                .then(function (response) {
                    that.wencaiData = response.data
                    // var i
                    // that.wencaiData = []
                    // for (i in response.data)
                    // {
                    //     that.wencaiData.push(i)
                    //     console.log(i)
                    // }  
                    that.loadingStatus = false
                    console.log(that.wencaiData)
                    console.log(that.wencaiData[1])
                    return that.wencaiData
                })
                .catch(function (error) {
                    console.log(error)
                })
            },
            getDataFromFilter() {
                console.log("getDataFromFilter")
            }
        },

    }
</script>