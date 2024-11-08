<script setup>
import {ElForm,ElFormItem,ElCol,ElInput,ElDatePicker,ElTimePicker,ElButton,ElRadio,} from "element-plus";
import { reactive } from 'vue'

// do not use same name with ref
const form = reactive({
  name: '',
  region: '',
  date1: '',
  date2: '',
  delivery: false,
  type: [],
  resource: '',
  desc: '',
})

const onSubmit = () => {
  console.log('submit!')
}
</script>

<template>
<div style="display: inline-block;margin-left: 100px">
  <el-form :model="form" label-width="auto" style="max-width: 600px">
    <el-form-item label="账单主题">
      <el-input v-model="form.name" />
    </el-form-item>
    <el-form-item label="账单金额">
      <el-input v-model="form.region" placeholder="请输入金额，保留两位小数">
      </el-input>
    </el-form-item>
    <el-form-item label="账单时间">
      <el-col :span="11">
        <el-date-picker
            v-model="form.date1"
            type="date"
            placeholder="Pick a date"
            style="width: 100%"
        />
      </el-col>
      <el-col :span="2" class="text-center">
        <span class="text-gray-500">-</span>
      </el-col>
      <el-col :span="11">
        <el-time-picker
            v-model="form.date2"
            placeholder="Pick a time"
            style="width: 100%"
        />
      </el-col>
    </el-form-item>
    <el-form-item label="角色">
      <el-radio-group v-model="form.resource">
        <el-radio value="付款人">付款人</el-radio>
        <el-radio value="分摊人">分摊人</el-radio>
      </el-radio-group>
    </el-form-item>
    <el-form-item label="活动具体描述">
      <el-input v-model="form.desc" type="textarea" placeholder="（选填）"/>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">提交</el-button>
    </el-form-item>
  </el-form>
</div>
</template>

<style scoped>

</style>