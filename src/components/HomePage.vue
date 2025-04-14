<template>
<div>
    <div>
        One Stop Solution for your Notes
    </div>
    <div class="textarea">
        <b-form-textarea
            id="textarea"
            v-model="text"
            placeholder="Enter something..."
            rows="10"
            max-rows="10"
        ></b-form-textarea>

    </div>
    <div class="submitbutton">
        <b-button variant="outline-primary" @click="submitNote">Button</b-button>
    </div>
</div>
</template>

<script>
import axios from 'axios';
export default{
    name: 'HomePage',
    data(){
        return {
            text:'',
        }
    },

    methods:{
        async submitNote(){
            try{
                await axios.post('http://127.0.0.1:5000/add_note',{
                    username: "Sujal Gupta",
                    note: this.text
                })
            }
            catch(err){
                console.log("Something went wrong",err);
                
            }

            this.text = ''
        }
    }
}
</script>

<style>
.textarea{
    width: 80%;
    margin: 0 auto;
    border: 2px solid black;
    border-radius: 4px;
}

.submitbutton{
    margin: 10px auto;
}
</style>