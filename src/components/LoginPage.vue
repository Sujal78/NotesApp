<template>
    <div>
        Login Page
        <div class = "input">
        <b-input-group prepend="Username" class="mt-1">
            <b-form-input v-model="username"></b-form-input>
        </b-input-group>
        </div>
        <div class = "input">
        <b-input-group prepend="Password" class="mt-1">
            <b-form-input v-model="password"></b-form-input>
        </b-input-group>
        </div>
        <div>
            <b-button :disabled="(username.length > 0 && password.length > 0)? false : true" variant="primary" class="signbutton" @click="handleClick">Login</b-button>
            <b-button class="signbutton" variant="outline-primary">Register</b-button>
        </div>
    </div>

</template>

<script>

export default{
    name: 'LoginPage',
    data(){
        return{
            username:'',
            password:'',
        }
    },
    methods:{
        handleClick(){
            console.log(this.username, this.password);
            this.$router.push('/user');
        }
    }
}


</script>

<style>

.signbutton{
    margin: 10px 10px;
}
.input{
    width: 50%;
    margin: 10px auto;
}
</style>