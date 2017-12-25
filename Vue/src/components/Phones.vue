<template lang="html">
  <div class="">
    <h1>Phones</h1>
    <router-link to="/">返回主页</router-link>
    <hr />

    <div v-for="item in message">
      <div class="box">
        <h3>{{ item.name }}</h3>
        <img :src="'http://localhost:8000' + item.images" alt="">
        <br />
        <span>￥{{ item.unit }}</span> <form action="/car" method="post"><button>加入购物车</button></form>
        <br />
      </div>
    </div>
  </div>
</template>


<script>
/* eslint-disable */
import axios from 'axios'
export default {
  data() {
    return {
      message: ''
    }
  },
  created() {
    axios.get('/phones').then((res) => {
      this.message = res.data
    })
  }
}
</script>

<style lang="css">
hr {
  border: 0.5px solid #E6E6E6;
}
button {
    height: 30px;
    background: #DE2626;
    border-radius: 3px;
    border: 0.8px solid #fff;
    font-size: 15px;
    color: #fff
}
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
  text-decoration: none;
}
span {
  color: #FF0000;
  font-size: 20px;
  font-weight: bold;
}
img {
  width: 90%;
}
.box {
  width: 80%;
  margin: 0 auto;
  border: 1px solid #E6E6E6;
  box-shadow: 0px 0px 20px  #E6E6E6;
  background: #FDFDFD;
  margin-top: 30px;
  border-radius: 8px;
}
</style>
