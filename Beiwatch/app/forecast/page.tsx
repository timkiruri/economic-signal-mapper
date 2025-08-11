"use client"

import { useEffect, useState } from 'react'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'
import { Badge } from '@/components/ui/badge'
import { apiClient, Product, ForecastResponse } from '@/lib/api'
import { TrendingUp, AlertCircle, Loader2 } from 'lucide-react'
import { useToast } from '@/hooks/use-toast'

export default function ForecastPage() {
  const [products, setProducts] = useState<Product[]>([])
  const [selectedProduct, setSelectedProduct] = useState<number | null>(null)
  const [forecast, setForecast] = useState<ForecastResponse | null>(null)
  const [loading, setLoading] = useState(false)
  const [productsLoading, setProductsLoading] = useState(true)
  const { toast } = useToast()

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const productsData = await apiClient.getProducts()
        setProducts(productsData)
      } catch (error) {
        console.error('Failed to fetch products:', error)
        toast({
          title: "Error",
          description: "Failed to load products",
          variant: "destructive",
        })
      } finally {
        setProductsLoading(false)
      }
    }

    fetchProducts()
  }, [toast])

  const handleForecast = async () => {
    if (!selectedProduct) return

    setLoading(true)
    try {
      const forecastData = await apiClient.getForecast(selectedProduct)
      setForecast(forecastData)
      toast({
        title: "Forecast Generated",
        description: "Price prediction has been calculated successfully",
      })
    } catch (error) {
      console.error('Failed to generate forecast:', error)
      toast({
        title: "Forecast Error",
        description: "Not enough historical data (minimum 30 days required)",
        variant: "destructive",
      })
      setForecast(null)
    } finally {
      setLoading(false)
    }
  }

  const selectedProductName = products.find(p => p.id === selectedProduct)?.name

  return (
    <div className="p-6 space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-foreground">Price Forecasting</h1>
        <p className="text-muted-foreground">
          Generate AI-powered price predictions using historical data
        </p>
      </div>

      {/* Forecast Input */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center space-x-2">
            <TrendingUp className="h-5 w-5" />
            <span>Generate Forecast</span>
          </CardTitle>
          <CardDescription>
            Select a product to predict its future price using our LSTM model
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="flex flex-col sm:flex-row gap-4">
            <div className="flex-1">
              <Select
                value={selectedProduct?.toString() || ""}
                onValueChange={(value) => setSelectedProduct(parseInt(value))}
                disabled={productsLoading}
              >
                <SelectTrigger>
                  <SelectValue placeholder="Select a product..." />
                </SelectTrigger>
                <SelectContent>
                  {products.map((product) => (
                    <SelectItem key={product.id} value={product.id.toString()}>
                      {product.name}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>
            <Button 
              onClick={handleForecast}
              disabled={!selectedProduct || loading}
              className="sm:w-auto w-full"
            >
              {loading ? (
                <>
                  <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                  Generating...
                </>
              ) : (
                <>
                  <TrendingUp className="mr-2 h-4 w-4" />
                  Generate Forecast
                </>
              )}
            </Button>
          </div>

          <div className="flex items-center space-x-2 text-sm text-muted-foreground">
            <AlertCircle className="h-4 w-4" />
            <span>Requires minimum 30 days of historical price data</span>
          </div>
        </CardContent>
      </Card>

      {/* Forecast Results */}
      {forecast && (
        <Card>
          <CardHeader>
            <CardTitle>Forecast Results</CardTitle>
            <CardDescription>
              AI-generated price prediction for {selectedProductName}
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div className="text-center p-6 bg-primary/5 rounded-lg">
                <div className="text-3xl font-bold text-primary mb-2">
                  KES {forecast.forecast_price.toFixed(2)}
                </div>
                <p className="text-sm text-muted-foreground">Predicted Price</p>
              </div>
              
              <div className="text-center p-6 bg-secondary/5 rounded-lg">
                <div className="text-3xl font-bold text-secondary-foreground mb-2">
                  {forecast.based_on_last_days}
                </div>
                <p className="text-sm text-muted-foreground">Days of Data Used</p>
              </div>
              
              <div className="text-center p-6 bg-accent/5 rounded-lg">
                <div className="text-3xl font-bold text-accent-foreground mb-2">
                  LSTM
                </div>
                <p className="text-sm text-muted-foreground">AI Model Used</p>
              </div>
            </div>

            <div className="mt-6 p-4 bg-muted/50 rounded-lg">
              <h4 className="font-medium mb-2">Forecast Details</h4>
              <div className="space-y-2 text-sm">
                <div className="flex justify-between">
                  <span className="text-muted-foreground">Product:</span>
                  <span>{selectedProductName}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-muted-foreground">Model Confidence:</span>
                  <Badge variant="secondary">High</Badge>
                </div>
                <div className="flex justify-between">
                  <span className="text-muted-foreground">Generated:</span>
                  <span>{new Date().toLocaleString()}</span>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>
      )}

      {/* Information Card */}
      <Card>
        <CardHeader>
          <CardTitle>How Price Forecasting Works</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <h4 className="font-medium mb-2">LSTM Neural Network</h4>
              <p className="text-sm text-muted-foreground">
                Our forecasting uses Long Short-Term Memory (LSTM) neural networks 
                trained on historical price data to predict future price movements.
              </p>
            </div>
            <div>
              <h4 className="font-medium mb-2">Data Requirements</h4>
              <p className="text-sm text-muted-foreground">
                Minimum 30 days of historical price data is required for accurate 
                predictions. More data generally leads to better forecasts.
              </p>
            </div>
            <div>
              <h4 className="font-medium mb-2">Accuracy</h4>
              <p className="text-sm text-muted-foreground">
                Forecasts are based on historical patterns and market trends. 
                Actual prices may vary due to external factors.
              </p>
            </div>
            <div>
              <h4 className="font-medium mb-2">Use Cases</h4>
              <p className="text-sm text-muted-foreground">
                Price forecasting helps with inventory planning, budget forecasting, 
                and identifying optimal purchase timing.
              </p>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
