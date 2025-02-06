import { createWebHistory, createRouter } from "vue-router";
import { useCookies } from "@vueuse/integrations/useCookies";
// import axios from 'axios';

const Home = () => import('../views/Home.vue');
const Login = () => import('../views/Login.vue');
const Main = () => import('../components/Main.vue');
const Create = () => import('../components/components_of_Main/create.vue');
const Check = () => import('../components/components_of_Main/check.vue');
const Clear = () => import('../components/components_of_Main/clear.vue');

const routes = [
    {
        path: "/",
        name: "home",
        component: Home,
        children: [
            {
                path: "/main",
                name: "main",
                component: Main,
                children: [
                    {
                        path: "/check",
                        name: "check",
                        component: Check,
                    },
                    {
                        path: "/create",
                        name: "create",
                        component: Create,
                    },
                    {
                        path: "/clear",
                        name: "clear",
                        component: Clear,
                    }
                ]
            }
        ]
    },
    {
        path: "/login",
        name: "login",
        component: Login
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

// For Login Authentication
router.beforeEach((to, from) => {
    const token = useCookies().get(["token"]);
    if(!token && to.name !== "login")  return {name: "login"};
    if(!token)  return;
    // verify token
})

export default router;