<template>
    <el-table :data="tableData" border stripe >
        <caption>Cookies View</caption>
        <el-table-column prop="name" label="Name" width="180"/>
        <el-table-column prop="value" label="value" width="280"/>

        <!-- 原版代码 -->
        <!-- <thead> 
            <tr>
                <th>Name</th>
                <th>Value</th>  
            </tr>
        </thead>
        <tbody>
            <tr v-for="(value, name) in cks.getAll()">
                <td>{{ name }}</td>
                <td>{{ value }}</td>
            </tr>
        </tbody> -->
    </el-table>
    <RouterView />
</template>

<script setup>
import { ElTable, ElTableColumn } from 'element-plus';
import { useCookies } from "@vueuse/integrations/useCookies"
const cks = useCookies();
cks.set("token", "testtoken");
const tableData = [{name: "token2", value: "testtoken2"},{name: "token1", value: "testtoken1"}]
</script>
