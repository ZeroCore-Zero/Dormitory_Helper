<template>
    <el-container>
        <el-header class="myheader">
            <el-text class="mytxt" type="primary">登录</el-text>
        </el-header>
        <el-main class="mymain">
            <el-form label-width="auto" class="login-form">
                <el-alert
                    title="登录注意事项"
                    type="info"
                    description="如已注册，可使用账户邮箱与密码登录，如未注册需先使用北邮网关账号登录以注册。"
                    show-icon
                />
                <el-form-item label="登录方式">
                    <el-select
                        v-model="form.login_opt"
                        placeholder="选择一种登录方式"
                        @change="value => {opt_hint = login_options.find(option => option.value === value).hint}"
                    >
                        <el-option
                            v-for="item in login_options"
                            :label="item.label"
                            :value="item.value"
                        />
                    </el-select>
                </el-form-item>
                <template v-if="form.login_opt">
                    <el-form-item label="用户名">
                        <el-input v-model="form.username" :placeholder="opt_hint" />
                    </el-form-item>
                    <el-form-item label="密码">
                        <el-input v-model="form.password" show-password placeholder="请输入密码" />
                    </el-form-item>
                    <el-form-item class="centered-item">
                        <div class="centered-checkbox">
                            <el-checkbox v-model="form.stay_login_in" label="保持登录" border />
                        </div>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="onSubmit" :loading="submit_loading" class="full-width">登录</el-button>
                    </el-form-item>
                </template>
            </el-form>
        </el-main>
    </el-container>
</template>

<script setup>
import { reactive, ref } from 'vue';
import {
    ElContainer, ElHeader, ElMain,
    ElForm, ElFormItem, ElSelect, ElOption, ElInput,
    ElText, ElButton, ElAlert,
    ElMessage, ElMessageBox, ElCheckbox
} from 'element-plus';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useCookies } from '@vueuse/integrations/useCookies';

const form = reactive({
    login_opt: "",
    username: "",
    password: "",
    stay_login_in: false
});
const opt_hint = ref();
const submit_loading = ref(false);
const router = useRouter();

const login_options = [
    {
        label: "账户登录",
        value: "default",
        hint: "请输入账户绑定邮箱"
    },
    {
        label: "北邮校园网登录",
        value: "bupt_net_login",
        hint: "请输入北邮学号"
    }
]

const onSubmit = () => {
    submit_loading.value = true;
    const payload_str = JSON.stringify(form);
    axios.post("/api/auth/login", JSON.parse(payload_str))
    .then(response => {
        useCookies().set("token", response.data["token"]);
        ElMessage({
            message: "登录成功，即将跳转",
            type: 'success',
            onClose: () => router.push({name: "home"})
        });
    })
    .catch(error => {
        console.log("There has an error:");
        console.log(error);
        let title, message, type;
        if(error.status === 401) {
            title = "错误";
            message = "用户名或密码错误，请检查填写是否正确或登陆方式选择错误";
            type = 'error';
        } else {
            title = "错误";
            message = "发生了一个错误，请稍后重试或联系管理员请求帮助";
            type = 'error';
        }
        ElMessageBox({title, message, type});
    })
    submit_loading.value = false;
}
</script>

<style>
.myheader {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 60px;
    text-align: center;
    background-color: #0073e6;
    border-bottom: 1px solid #ddd;
    padding: 10px 20px;
    color: white;
    font-size: 24px;
    font-weight: bold;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    margin: 5px;

}

.mytxt {
    font-size: 22px;
    font-weight: bold;
    color: white;
}

.mymain {
    padding: 20px;
    background-color: #fff;
    min-height: 100vh;
}

.login-form {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.alert-box {
    margin-bottom: 20px;
}

.full-width {
    width: 100%;
}

.centered-item {
    display: flex;
    justify-content: center;
}

.centered-checkbox {
    display: flex;
    justify-content: center;
    width: 100%;
}

</style>
