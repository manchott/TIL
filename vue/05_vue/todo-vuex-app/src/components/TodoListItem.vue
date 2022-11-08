<template>
  <div>
    <span 
      @click="updateTodoStatus"
      :class="{ 'is-completed': todo.isCompleted }"
    >{{ todo.title }}</span>
    <button @click="deleteTodo">Delete</button>
  </div>
</template>

<script>
export default {
  name: "TodoListItem",
  props: {
    todo: Object,
  },
  methods: {
    deleteTodo(){
      // console.log("press button")
      this.$store.dispatch('deleteTodo', this.todo)
      // this.$store.commit('DELETE_TODO', this.todo) 바로 mutations으로 가기 가능

    },
    updateTodoStatus() {
      this.$store.dispatch('updateTodoStatus', this.todo)
    }
  }

}
</script>

<style>
  .is-completed {
    text-decoration: line-through;
  }
</style>