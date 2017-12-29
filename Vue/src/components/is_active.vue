<template lang="html">
  <h1>验证成功</h1>
</template>

<script>
/* eslint-disable */
import axios from 'axios'
export default {
  data() {
    return {

    }
  },
  created() {
    axios.post('/is_active').then((res) => {
      console.log(res.data);
    })
  }
}
</script>

<style lang="css">
</style>
