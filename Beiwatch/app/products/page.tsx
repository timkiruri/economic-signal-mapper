"use client"

import { useEffect, useState } from 'react'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { apiClient, Product, Category, Price } from '@/lib/api'
import { Search, Package } from 'lucide-react'

export default function ProductsPage() {
  const [products, setProducts] = useState<Product[]>([])
  const [categories, setCategories] = useState<Category[]>([])
  const [prices, setPrices] = useState<Price[]>([])
  const [searchTerm, setSearchTerm] = useState('')
  const [selectedCategory, setSelectedCategory] = useState<number | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [productsData, categoriesData, pricesData] = await Promise.all([
          apiClient.getProducts(),
          apiClient.getCategories(),
          apiClient.getPrices()
        ])
        setProducts(productsData)
        setCategories(categoriesData)
        setPrices(pricesData)
      } catch (error) {
        console.error('Failed to fetch products:', error)
      } finally {
        setLoading(false)
      }
    }

    fetchData()
  }, [])

  const filteredProducts = products.filter(product => {
    const matchesSearch = product.name.toLowerCase().includes(searchTerm.toLowerCase())
    const matchesCategory = selectedCategory === null || product.category_id === selectedCategory
    return matchesSearch && matchesCategory
  })

  const getProductPrices = (productId: number) => {
    return prices.filter(price => price.product_id === productId)
  }

  const getCategoryName = (categoryId?: number) => {
    if (!categoryId) return 'Uncategorized'
    const category = categories.find(c => c.id === categoryId)
    return category?.name || 'Unknown'
  }

  const getLatestPrice = (productId: number) => {
    const productPrices = getProductPrices(productId)
    if (productPrices.length === 0) return null
    
    return productPrices.reduce((latest, current) => 
      new Date(current.timestamp) > new Date(latest.timestamp) ? current : latest
    )
  }

  if (loading) {
    return (
      <div className="p-6">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {[...Array(6)].map((_, i) => (
            <Card key={i}>
              <CardHeader className="animate-pulse">
                <div className="h-4 bg-muted rounded w-3/4"></div>
                <div className="h-3 bg-muted rounded w-1/2"></div>
              </CardHeader>
            </Card>
          ))}
        </div>
      </div>
    )
  }

  return (
    <div className="p-6 space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-foreground">Products</h1>
        <p className="text-muted-foreground">
          Browse and search tracked products
        </p>
      </div>

      {/* Search and Filters */}
      <div className="flex flex-col sm:flex-row gap-4">
        <div className="relative flex-1">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-muted-foreground" />
          <Input
            placeholder="Search products..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="pl-10"
          />
        </div>
        <div className="flex gap-2 flex-wrap">
          <Button
            variant={selectedCategory === null ? "default" : "outline"}
            onClick={() => setSelectedCategory(null)}
            size="sm"
          >
            All Categories
          </Button>
          {categories.map((category) => (
            <Button
              key={category.id}
              variant={selectedCategory === category.id ? "default" : "outline"}
              onClick={() => setSelectedCategory(category.id)}
              size="sm"
            >
              {category.name}
            </Button>
          ))}
        </div>
      </div>

      {/* Products Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {filteredProducts.map((product) => {
          const latestPrice = getLatestPrice(product.id)
          const productPrices = getProductPrices(product.id)
          
          return (
            <Card key={product.id} className="hover:shadow-md transition-shadow">
              <CardHeader>
                <div className="flex items-start justify-between">
                  <div className="flex items-center space-x-2">
                    <Package className="h-5 w-5 text-muted-foreground" />
                    <div>
                      <CardTitle className="text-lg">{product.name}</CardTitle>
                      <CardDescription>
                        {getCategoryName(product.category_id)}
                      </CardDescription>
                    </div>
                  </div>
                </div>
              </CardHeader>
              <CardContent>
                <div className="space-y-3">
                  {latestPrice ? (
                    <div>
                      <div className="text-2xl font-bold text-primary">
                        KES {latestPrice.price.toFixed(2)}
                      </div>
                      <p className="text-xs text-muted-foreground">
                        Last updated: {new Date(latestPrice.timestamp).toLocaleDateString()}
                      </p>
                    </div>
                  ) : (
                    <div className="text-muted-foreground">No price data available</div>
                  )}
                  
                  <div className="flex justify-between items-center">
                    <Badge variant="secondary">
                      {productPrices.length} price records
                    </Badge>
                    <Button size="sm" variant="outline">
                      View Details
                    </Button>
                  </div>
                </div>
              </CardContent>
            </Card>
          )
        })}
      </div>

      {filteredProducts.length === 0 && (
        <div className="text-center py-12">
          <Package className="h-12 w-12 text-muted-foreground mx-auto mb-4" />
          <h3 className="text-lg font-medium text-foreground mb-2">No products found</h3>
          <p className="text-muted-foreground">
            Try adjusting your search terms or category filters
          </p>
        </div>
      )}
    </div>
  )
}
