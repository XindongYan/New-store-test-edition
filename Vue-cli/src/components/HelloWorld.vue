<template>
  <div class="hello">
      <h1>{{ msg }}</h1>
      <router-link v-show='sign' to='/login'><button type="button">登陆</button></router-link>

      <h3 v-if="seen">{{ session }}</h3>
      <p v-show="n">{{ nul }}</p>

      <form action="/signout" method="post">
        <button v-show='signout'>
            <router-link to="/signout"><a style="color:#495060">登出</a></router-link>
        </button>
      </form>
    <br />

    <hr>
    <div class="box">
      <router-link to="/phones">
      <a href="/phones">
        <h3>Phones</h3>
        <img :src="'http://localhost:8000/media/media/' + 'phones.png'" alt="">
        <h3></h3>
      </a>
      </router-link>
    </div>

    <router-link to="/thing">
    <div class="box">
      <h3>小物件</h3>
      <img :src="'http://localhost:8000/media/thing/' + 'music.png'" alt="">
      <h3></h3>
    </div>
  </router-link>

    <div class="box">
      <router-link to="/mac">
      <h3>Mac</h3>
      <img :src="'http://localhost:8000/media/pc/' + 'imacpro.png'" alt="">
      <h3></h3>
      </router-link>
    </div>

    <div class="box">

    </div>

  </div>
</template>

<script>
/* eslint-disable */

import axios from 'axios'
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Vue.js App',
      message: '',
      session: '',
      seen: true,
      nul: '',
      n: false,
      signout: '',
      sign: true
    }
  },

  created() {
    axios.get('/session').then((res) => {
      if (res.data == 'null'){
        this.nul = 'null'
        this.seen = false
        this.sign = true
        this.signout = false
      }
      if (res.data != 'null') {
      this.session = res.data
      this.sign = false
      this.signout = true
    }
    })
  },

  method: {
    prt() {
        axios.post('/signout', {
        }).then((res) => {
            //
        })
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
hr {
  border: 0.5px solid #E6E6E6;
}
button {
    height: 30px;
    width: 70px;
    background: #fff;
    border-radius: 3px;
    border: 0.8px solid #ccc;
    font-size: 15px
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
  color: #160F0F;
  text-decoration: none;
}
span {
  color: #FF0000;
  font-size: 17px;
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
