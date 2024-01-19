<template>
  <div id="app" class="container mt-4">
    <InputRow
      v-for="(item, index) in items"
      :key="index"
      :item="item"
      :index="index"
      :checkAndFetchParent="checkAndFetch"
    />
    <div class="row mb-3">
      <div class="col">
        <button @click="addRow" class="btn btn-success">+</button>
        <button
          v-if="items.length > 1"
          @click="deleteRow"
          class="btn btn-danger"
        >
          -
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import InputRow from "./components/InputRow.vue";

export default {
  components: {
    InputRow,
  },
  data() {
    return {
      items: [{ acronym: "", code: "", concentration: "" }],
    };
  },
  methods: {
    checkAndFetch(index, updatedItem) {
      this.items[index] = updatedItem;
      const acronyms = [];
      const codes = [];
      this.items.forEach((element) => {
        acronyms.push(element.acronym);
        codes.push(element.code);
      });

      const dataToSend = { acronyms: acronyms, codes: codes };
      axios
        .post("http://127.0.0.1:5000/api/predict", dataToSend, {
          headers: {
            "Content-Type": "application/json",
          },
        })
        .then((response) => {
          for (let i = 0; i < response.data.length; i++) {
            this.items[i] = response.data[i];
          }
        })
        .catch((error) => {
          console.error("Erro ao obter concentração:", error);
        });
    },
    addRow() {
      this.items.push({ acronym: "", code: "", concentration: "" });
    },
    deleteRow() {
      this.items.splice(this.items.length - 1);
    },
  },
};
</script>

<style>
.form-row {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

input {
  margin-right: 10px;
}
</style>
