<template>
    <table>
        <caption>Cookies View</caption>
        <thead>
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
        </tbody>
    </table>
    <RouterView />
</template>

<script setup>
import { useCookies } from "@vueuse/integrations/useCookies"
const cks = useCookies();
// cks.set("token", "testtoken");
</script>