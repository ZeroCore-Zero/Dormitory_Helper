<template>
    <el-table v-if="_DEBUG" :data=cks_view border stripe >
        <caption>Cookies View</caption>
        <el-table-column prop="name" label="Name" />
        <el-table-column prop="value" label="Value" />
    </el-table>
    <RouterView />
</template>

<script setup>
import { ElTable, ElTableColumn } from 'element-plus';
import { useCookies } from "@vueuse/integrations/useCookies"

const _DEBUG = true;
const cks = useCookies();
const cks_view = Object.keys(cks.getAll()).map(key => {
    return {name: key, value: cks.getAll()[key]}
})
</script>
