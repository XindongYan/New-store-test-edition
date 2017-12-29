<template>
    <div>
        <h1>{{ msg }}</h1>
        <form action="/register" method="post">
            <br />
            <br />
            <label for="">用户名:</label>&nbsp&nbsp&nbsp&nbsp&nbsp
            <input type="text" required="required" name="username" placeholder="输入你的用户名">
            <br>
            <br />
            <label for="">邮箱:</label>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
            <input type="email" required="required" name="email" placeholder="邮箱">
            <br />
            <br />
            <label for="">密码:</label>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
            <input id="password" type="password" required="required" name="password" placeholder="密码">
            <br />
            <br />
            <label for="">再次输入:</label>&nbsp
            <input v-model="repsd" id="re_password" required="required" type="password" name="re_password" placeholder="再次输入">
            <br />
            <br />
            <input style="height: 30px; width: 100px; background:#2d8cf0; color:#fff" type="submit" value="提交"> {{ message }}
        </form>
    </div>
</template>

<script>
    /* eslint-disable */
    import axios from 'axios'
    export default {
        name: 'Exp_2',
        data() {
            return {
                msg: '注册',
                message: '',
                repsd: ''
            }
        },
        created() {
        },
        methods: {
            prt() {
                axios.post('/register', {
                }).then((res) => {
                    //
                })
            },
        }
    }

</script>

<style>
    input {
        height: 35px;
        width: 200px;
        border-radius: 8px;
        border: 0.5px solid #cccccc;
    }

    input::-webkit-input-placeholder {
        text-align: center;
    }

    div {
        text-align: center;
        height: auto;
        margin: 0 auto;
        margin-top: 150px
    }
</style>
