<template>
<div>
    <h1>Game Over</h1>
    <h2>Your score is {{score}}</h2>
    <h2>Your high score is {{highScore}}</h2>
    <button @click="$emit('change-view', 'Game')">Play Again</button>
</div>
</template>

<script>
export default {
    props: {
        score: Number,
        highScore: Number
    }
}
</script>


