import { createWebHistory, createRouter } from "vue-router";
import { useCookies } from "@vueuse/integrations/useCookies";
// import axios from 'axios';

const Home = () => import('../views/Home.vue');
const Login = () => import('../views/Login.vue');

const routes = [
    {
        path: "/",
        name: "home",
        component: Home
    },
    {
        path: "/login",
        name: "login",
        component: Login
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

// For Login Authentication
router.beforeEach((to, from) => {
    const token = useCookies().get(["token"]);
    console.log("token is: " + token);
    if(!token && to.name !== "login")  return {name: "login"};
    if(!token)  return;
    // verify token
})

export default router;