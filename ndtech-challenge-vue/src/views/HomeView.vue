<template>
    <div class="container">
        <SidePanel>
            <SearchPanel :v-if="searchPanelMounted" @mounted="onSearchPanelMounted"/>
        </SidePanel>
        <MainPanel>
            <TablePanel :v-if="searchPanelMounted"/>
        </MainPanel>
    </div>
</template>

<script setup>
import { ref } from "vue"
import SidePanel from "../components/SidePanel.vue"
import MainPanel from "../components/MainPanel.vue"
import SearchPanel from "../components/home/SearchPanel.vue"
import TablePanel from '../components/home/TablePanel.vue'

const searchPanelMounted = ref(false);

const onSearchPanelMounted = () => {
    searchPanelMounted.value = true;
};

</script>

<style scoped>
.container {
    margin-top: 70px;
    background-color: white;
    display: flex;
    flex-direction: row;
    height: 100%;
}
</style>