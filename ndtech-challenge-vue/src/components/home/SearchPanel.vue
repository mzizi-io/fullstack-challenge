<template>
    <div class="side-panel-search-container">
        <div class="side-panel-search-header">
            <h2 class="side-panel-search-header-text">ASSET EXPLORER</h2>
        </div>

        <div>
            <v-text-field label="Full Address" v-model="fullAddress"></v-text-field>

            <v-text-field label="Class Description" v-model="classDescription"></v-text-field>


            <v-container>
                <p class="label-text">Estimated Value</p>
                <v-range-slider
                    v-model="estimatedValue"
                    step="1"
                    :min="0"
                    :max="maxEstVal"
                    thumb-label="always"
                     color="#0C2F57"
                ></v-range-slider>
            </v-container>

            <v-autocomplete
                label="Building Use (BLDG_USE)"
                v-model="buildingUse"
                :items="buildingUseOptions"
            ></v-autocomplete>
            
            <v-container>
                <p class="label-text">Building SQ FT</p>
                <v-range-slider
                    v-model="buildingSqFT"
                    color="#0C2F57"
                    step="1"
                    :min="0"
                    :max="maxBuildingSqFT"
                    thumb-label="always"
                ></v-range-slider>
            </v-container>
        </div>
        <v-btn prepend-icon="mdi-magnify" @click="getSearchedAssets(true)">Find Asset</v-btn>

    </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { search } from '../../utils/services';
import { useGlobalStore } from '../../utils/store';
import { getDistinctValues, getMaxValue } from '../../utils/services';

const store = useGlobalStore()

const defaultVal = 10000
const toggle = ref("")
var maxEstVal = ref(defaultVal)
var maxBuildingSqFT = ref(defaultVal)
var estimatedValue = ref([0, defaultVal])
var buildingSqFT = ref([0, defaultVal])
var fullAddress = ref("")
var classDescription = ref("")
var buildingUse = ref("")
var buildingUseOptions = ref([])


const fields = {
    textFields: {
        fullAddress: {
            minSearchLen: 5,
            dbField: "full_address",
            value: fullAddress
        },
        classDescription: {
            minSearchLen: 5,
            dbField: "class_description",
            value: classDescription
        }
    },
    numericFields: {
        estimatedValue: {
            value: estimatedValue,
            dbField: "estimated_market_value"
        },
        buildingSqFT: {
            value: buildingSqFT,
            dbField: "building_sq_ft"         
        }
    }
}

const getFieldOptions = async() => {
    const opt = await getDistinctValues("bldg_use")
    const maxMktVal = await getMaxValue("estimated_market_value")
    const maxSqF = await getMaxValue("building_sq_ft")
    if (opt) buildingUseOptions.value = opt
    if (maxMktVal) maxEstVal.value = maxMktVal
    if (maxSqF) maxBuildingSqFT.value = maxSqF
}

const createTextFilter = (item) => {
    if (item.value.value.length >= item.minSearchLen){
        return {
            field: item.dbField,
            value: item.value.value,
            searchType: "string"
        }
    }
}

const getTextFilterParams = () => {
    const params = []
    Object.keys(fields.textFields).forEach((key) => {
        const res = createTextFilter(fields.textFields[key])
        if (res) params.push(res)
    })
    return params
}

const getSearchedAssets = async(includeNumericVals) => {
    const params = getTextFilterParams()

    if (buildingUse.value){
        params.push({
            field: "bldg_use",
            value: buildingUse.value,
            searchType: "exact_string"
        })
    }
    
    if (includeNumericVals){
        if (estimatedValue.value[1] !== defaultVal || estimatedValue.value[0] !== 0 ) {
            params.push({
                field: "estimated_market_value",
                min: estimatedValue.value[0],
                max: estimatedValue.value[1],
            })
        }
        if (buildingSqFT.value[1] !== defaultVal || buildingSqFT.value[0] !== 0 ) {
            params.push({
                field: "building_sq_ft",
                min: buildingSqFT.value[0],
                max: buildingSqFT.value[1],
            })
        }
    }

    const body = {
        "params": params, 
        page: store.page,
        per_page: store.perPage
    }

    if (params.length > 0) {
        const _assets = await search(body) 
        if (_assets !== null) store.setAssets(_assets.assets)
    }
}

onMounted( getFieldOptions )
watch(
    [estimatedValue, buildingSqFT, fullAddress, classDescription, buildingUse],
    async () => {getSearchedAssets(false)}
)
</script>

<style scoped>
.side-panel-search-container {
    width: 100%;
    height: 100%;
    color: #0C2F57;
    align-items: "center";
    padding: 1rem;
}
.side-panel-search-header {
    height: 15%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.side-panel-search-header-text {
    text-shadow: 1px 1px 2px #41B6E6;
    font-size: 1.7rem;
}
.side-panel-search-header-text:hover {
  color: #41B6E6;
  text-shadow: 1px 1px 2px #0C2F57;
}
.label-text {
    color: #757575;
    text-align: left;
    margin-bottom: 2rem;
}
.buttons{
    width: 100%;
    display: flex;
    flex-direction: row;
    align-items: baseline;
    gap: 1rem;
}
</style>