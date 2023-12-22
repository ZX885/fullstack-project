import './style.scss'
import { useState, useEffect } from 'react'
import { getFurniture } from '../../conf/common'
import Item from './item'

function Products() {
    const [furnitures, setFurnitures] = useState([])

    useEffect(() => {
        getFurniture().then((data) => {
            setFurnitures(data)
        })
    }, [])

    return (
        <div id="product-page">
            <h1>Latest Products</h1>

            <div className="new-arrivals">
                <ul>
                    <li>New Arrival</li>
                    <li>Best Seller</li>
                    <li>Featured</li>
                    <li>Special Offer</li>
                </ul>
            </div>

            <div className="items">
                {
                    furnitures && furnitures.map((furniture, index) => {
                        return (
                            <Item 
                                key={index}
                                price={furniture.price}
                                image={furniture.image}
                                name={furniture.name}
                                itemID={furniture.id}
                            />
                        )
                    })
                }
            </div>
        </div>
    );
}

export default Products;