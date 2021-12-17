<template>
<div>
    <h1>Game Over</h1>
    <h2>Your score is {{score}}</h2>
    <button @click="$emit('change-view', 'Game')">Play Again</button>
</div>
</template>

<script>
export default {
    props: {
        score: Number
    }
}
</script>


