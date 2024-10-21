<template>
    <el-container>
        <el-header>
            5T09_Helper
        </el-header>
        <el-main>
            <el-tabs tab-position="left" model-value="name1">
                <el-tab-pane label="AA统计" name="name1">
                    <Bill />
                </el-tab-pane>
                <el-tab-pane label="电费监测" name="name2">正在开发</el-tab-pane>
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
</style>