<template>
    <div>
        <h1>{{ msg }}</h1>
        <form action="/login" method="post">
            <br />
            <br />
            <label for="">用户名:</label>&nbsp&nbsp&nbsp&nbsp&nbsp
            <input type="text" name="username" placeholder="输入你的用户名">
            <br>
            <br />
            <label for="">密码:</label>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
            <input type="password" name="password" placeholder="密码">
            <br />
            <br />
            <input style="height: 30px; width: 70px; background:#2d8cf0; color:#fff" type="submit" @click='greet' value="提交">
        </form>
        <br>
        <hr style="width:25%">
        <span style="font-size:14px; color:#80848f">或者</span>
        <button>
            <router-link to="/register"><a style="color:#495060" href="/register">注册</a></router-link>
        </button>
        </router-link>
    </div>
</template>

<script>
    /* eslint-disable */
    import axios from 'axios'

    export default {
        name: 'Exp_1',
        data() {
            return {
                msg: "登陆"
            }
        },

        methods: {
            prt() {
                axios.post('/login', {
                }).then((res) => {
                    //
                })
            },
            greet: (event) => {

            }
        }
    }

</script>

<style>
    a {
        text-decoration: none
    }

    input {
        height: 35px;
        width: 200px;
        border-radius: 3px;
        border: 0.5px solid #cccccc;
    }

    input::-webkit-input-placeholder {
        text-align: center;
    }

    button {
        height: 30px;
        width: 70px;
        background: #fff;
        border-radius: 3px;
        border: 0.8px solid #ccc;
        font-size: 15px
    }

    div {
      margin-top: 150px;
    }
</style>
