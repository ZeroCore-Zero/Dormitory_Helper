<template>
    <el-container class="container">

        <el-header>
            <div>
                <img src="../../photo/logo.png" width="56" height="56">
                <!-- 这里是校徽图片，网页中的header的width为56.6 -->
                <span>
                    电商后台管理系统
                </span>
            </div>
        </el-header>

        <el-main class="main-content">
            <el-tabs tab-position="left" model-value="name1">
                <el-tab-pane label="AA统计" name="name1">
                    <Bill />
                </el-tab-pane>
                <el-tab-pane label="电费监测" name="name2"> 
                    正在开发 
                </el-tab-pane>
            </el-tabs>
        </el-main>

    </el-container>
</template>

<script setup>
    import {ElTabs, ElTabPane, ElContainer, ElHeader, ElMain} from 'element-plus';
    import Bill from '../components/Bill.vue';
</script>

<style>
.el-tab-pane {
    word-break: break-all;
    word-wrap: break-word;
}


.el-header {
    background-color: #c8e8f5;
    display: flex;
    color: #1860e6;
    font-size: 25px;
    padding: 10px 20px; 
    border-top-left-radius: 10px; 
    border-top-right-radius: 10px;
    border-bottom: 5px solid #cae2fc;
    margin-bottom: 10px;
}

.el-header div {
    display: flex;
    align-items: center;
}

.el-header span {
    margin-left: 15px;
}

.container {
    background-color: #b1d3fc;
    padding: 35px; 
    border-radius: 10px; 
    margin: 5px;
    overflow: hidden;
}

.main-content {
    padding: 20px;
    background-color: #b1d3fc;
    border-radius: 10px;
    margin-top: 10px;
}
</style>
