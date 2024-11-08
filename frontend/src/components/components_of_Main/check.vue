<script setup lang="ts">
import {
  ElTable,
  ElTableColumn,
  ElInput,
  ElForm,
  ElRadio,
  ElButton, ElFormItem,ElMain,
} from 'element-plus';

interface User{
    id:number;
    date:string;
    name:string;
    topic:string;
    actor: "付款人"|"分摊人";
    statement: 'warning-row'|'success-row'|'';
    money:number;
  }

const tableData: User[]=[
  {
    id:1,
    date: 'XXX',
    name: '刘浩天',
    topic: '给宿舍带饭',
    actor: '付款人',
    statement: 'warning-row',
    money:50
  },
  {
    id:2,
    date: 'XXXX',
    name: '刘浩天',
    topic: '宿舍用电',
    actor: '分摊人',
    statement: 'success-row',
    money:24
  },
  {
    id:3,
    date: 'XXXXX',
    name: 'XXXXX',
    topic: 'XXXXX',
    actor: 'XXXXX',
    statement: '',
    money:89
  },
  {
    id:4,
    date: 'XXXXX',
    name: 'XXXXX',
    topic: 'XXXXX',
    actor: 'XXXXX',
    statement: '',
    money:89
  },
  {
    id:5,
    date: 'XXXXX',
    name: 'XXXXX',
    topic: 'XXXXX',
    actor: 'XXXXX',
    statement: '',
    money:89
  },
  {
    id:6,
    date: 'XXXXX',
    name: 'XXXXX',
    topic: 'XXXXX',
    actor: 'XXXXX',
    statement: '',
    money:89
  },
  {
    id:7,
    date: 'XXXXX',
    name: 'XXXXX',
    topic: 'XXXXX',
    actor: 'XXXXX',
    statement: '',
    money:89
  },
  {
    id:8,
    date: 'XXXXX',
    name: 'XXXXX',
    topic: 'XXXXX',
    actor: 'XXXXX',
    statement: '',
    money:89
  },
  {
    id:9,
    date: 'XXXXX',
    name: 'XXXXX',
    topic: 'XXXXX',
    actor: 'XXXXX',
    statement: '',
    money:89
  },
  {
    id:10,
    date: 'XXXXX',
    name: 'XXXXX',
    topic: 'XXXXX',
    actor: 'XXXXX',
    statement: '',
    money:89
  },
  {
    id:11,
    date: 'XXXXX',
    name: 'XXXXX',
    topic: 'XXXXX',
    actor: 'XXXXX',
    statement: '',
    money:89
  },
]

const tableRowClassName = ({row}: {
  row: User
}) => {
  if (row.statement==='warning-row') {
    return 'warning-row'
  } else if (row.statement==='success-row') {
    return 'success-row'
  }
  return ''
}
</script>

<template>
  <div style="display: inline-block;margin-left: 200px">
    <el-main>
            <el-table :data="tableData"
                      style="width: auto"
                      :row-class-name="tableRowClassName"
                      height="400px">
              <el-table-column fixed prop="date" label="日期" width="180"/>
              <el-table-column prop="id" label="编号" width="180"/>
              <el-table-column prop="name" label="姓名" width="180"/>
              <el-table-column prop="topic" label="主题" width="180"/>
              <el-table-column prop="money" label="金额" width="180"/>
              <el-table-column prop="actor" label="作为" width="180"/>
            </el-table>
    </el-main>
  </div>
<!--  <br>-->
<!--  <div style="margin-left: 200px">-->
<!--    <el-main>-->
<!--    <el-form :model="form" label-width="auto" style="max-width: 600px">-->
<!--      <el-form-item label="选择账单">-->
<!--        <el-input v-model="form.name" placeholder="写入编号"/>-->
<!--      </el-form-item>-->
<!--      <el-radio-group v-model="form.resource">-->
<!--        <el-radio value="付款人">通过</el-radio>-->
<!--        <el-radio value="分摊人">不通过</el-radio>-->
<!--      </el-radio-group>-->
<!--      <el-form-item>-->
<!--        <el-button type="primary" @click="onSubmit">提交</el-button>-->
<!--      </el-form-item>-->
<!--    </el-form>-->
<!--    </el-main>-->
<!--  </div>-->
</template>

<style scoped>
.el-table .warning-row {
  --el-table-tr-bg-color: var(--el-color-warning-light-9);
}
.el-table .success-row {
  --el-table-tr-bg-color: var(--el-color-success-light-9);
}
</style>