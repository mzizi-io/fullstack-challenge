const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export async function getAssets(page, perPage){
    const response = await fetch(`${API_BASE_URL}/v1/search/${page}/${perPage}`)
    return response.json()
}

export async function getCount(){  
    const response = await fetch(`${API_BASE_URL}/v1/stats/count`)
    return response.json()
}

export async function getDistinctValues(field){  
    const response = await fetch(`${API_BASE_URL}/v1/stats/distinct-values/by-field/${field}`)
    return response.json()
}

export async function getMaxValue(field){  
    const response = await fetch(`${API_BASE_URL}/v1/stats/max/by-field/${field}`)
    return response.json()
}

export async function search(searchParams){
    const response = await fetch(`${API_BASE_URL}/v1/search/`, {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(searchParams)
    })
    return response.json() 
}