<template>
  <div class="row mb-3">
    <div class="col">
      <input
        v-model="localItem.acronym"
        @blur="handleBlur"
        placeholder="Acrônimo"
        class="form-control"
      />
    </div>
    <div class="col">
      <input
        v-model="localItem.code"
        @blur="handleBlur"
        placeholder="Código"
        class="form-control"
      />
    </div>
    <div class="col">
      <input
        v-model="localItem.concentration"
        placeholder="Concentração"
        class="form-control"
      />
    </div>
  </div>
</template>

<script>
export default {
  props: {
    item: Object,
    index: Number,
    addRow: Function,
    deleteRow: Function,
    checkAndFetchParent: Function,
  },
  data() {
    return {
      localItem: { ...this.item },
    };
  },
  computed: {
    isLastRow() {
      return this.index === this.$parent.items.length - 1;
    },
  },
  methods: {
    handleBlur() {
      const { localItem, index } = this;
      if (localItem.acronym && localItem.code) {
        this.checkAndFetchParent(index, localItem);
      }
    },
  },
  watch: {
    item() {
      this.localItem = { ...this.item };
    },
  },
};
</script>
