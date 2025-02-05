<template>
    <div class="table-container">
        <v-btn-toggle v-model="toggle">
            <v-btn icon="mdi-map" value="map"></v-btn>
            <v-btn icon="mdi-table" value="table"></v-btn>
        </v-btn-toggle>

        <v-data-table-server
            v-if="toggle==='table'"
            :headers="config.tableHeaders"
            :items="store.assets"
            v-model:items-per-page="perPage"
            v-model:page="page"
            :items-length="store.pageCount"
            class="elevation-1"
        ></v-data-table-server>

        <div v-if="toggle==='map'" style="height: 95%; width: 100%;">
            <l-map
                v-model:zoom="zoom"
                :center="center"
                :use-global-leaflet="false"
                @update:bounds="updateBounds"
                @moveend="getAssetsFromCoordinates"
                @zoomend="getAssetsFromCoordinates"
                style="height: 100%; width: 100%;border: 1px solid black"
            >
            <l-tile-layer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"></l-tile-layer>

            <l-marker v-for="(marker, index) in markers" :key="index" :lat-lng="marker.position">
                <l-popup :options="{ width: 300, height: 300 }"> 
                    <h2>PIN: {{ marker.name }}</h2>
                    <p>Address: {{marker.address}}</p>
                    <p>{{marker.description}}</p>
                </l-popup>
            </l-marker>

          </l-map>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, watch, computed } from "vue";
import { getAssets, getCount, search } from "../../utils/services";
import { useGlobalStore } from "../../utils/store";
import config from "../../utils/config";
import { LMap, LTileLayer, LMarker, LPopup } from "@vue-leaflet/vue-leaflet";
import "leaflet/dist/leaflet.css";

const store = useGlobalStore();

const toggle = ref("table")
const zoom = ref(10);
const center = ref([41.8781, -87.6298]);
const bounds = ref({ northEast: null, southWest: null });

const updateBounds = (newBounds) => {
    console.log(newBounds)
  bounds.value = {
    northEast: [newBounds._northEast.lat, newBounds._northEast.lng],
    southWest: [newBounds._southWest.lat, newBounds._southWest.lng],
  };
};

const markers = ref([]);


const getAssetsFromCoordinates = async () => {
    const body = {
        params: [{
            field: "latitude",
            min: Math.min(bounds.value.northEast[0], bounds.value.southWest[0]),
            max: Math.max(bounds.value.northEast[0], bounds.value.southWest[0]),
        },{                                                              
            field: "longitude",
            min: Math.min(bounds.value.northEast[1], bounds.value.southWest[1]),
            max: Math.max(bounds.value.northEast[1], bounds.value.southWest[1]),                                     
        }],
        page: 1,
        per_page: 100                                                  
    }
    console.log(body)
    const _assets = await search(body)                                                                                                                      
    store.setAssets(_assets.assets)
    await updateMarkers()
}

const updateMarkers = async () => {
    const newMarkers = []
    store.assets.map(row => {
        newMarkers.push({
            position: [row.latitude, row.longitude],
            name: row.pin,
            address: row.full_address,
            description: row.class_description
        })
    })
    markers.value = newMarkers
}

const fetchAssets = async () => {
    const _assets = await getAssets(page.value, perPage.value)
    store.setAssets(_assets.assets)
}

onMounted( async() => {
    await fetchAssets()
    const _count = await getCount()
    store.setPageCount(_count)
    await updateMarkers()
})

const page = computed({
    get: () => store.page,
    set: (newVal) => store.setPage(newVal)
})

const perPage = computed({
    get: () => store.perPage,
    set: (newVal) => store.setPerPage(newVal)
})

watch([perPage, page], fetchAssets )
watch([zoom, center], getAssetsFromCoordinates)
</script>

<style>
@import "leaflet/dist/leaflet.css";
.table-container{
    height: 100%;
    width:100%;
    padding: 1rem;
    padding-top: 2rem;
    overflow: scroll;
}

</style>