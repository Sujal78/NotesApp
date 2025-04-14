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

        <pre class="mt-3 mb-0">{{ text }}</pre>
    </div>
</div>
</template>

<script>
export default{
    name: 'HomePage',
    data(){
        return {

        }
    },

    methods:{

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
</style>