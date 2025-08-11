'use client'

import { useEffect, useState } from 'react'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Package, Store, TrendingUp } from 'lucide-react'
import { PriceChart } from '@/components/price-chart'
import { apiClient, Price } from '@/lib/api'

export default function Dashboard() {
  const [stats, setStats] = useState({
    totalProducts: 0,
    totalRetailers: 0,
    totalPrices: 0
  })
  const [recentPrices, setRecentPrices] = useState<Price[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [products, retailers, prices] = await Promise.all([
          apiClient.getProducts(),
          apiClient.getRetailers(),
          apiClient.getPrices()
        ])

        // Set stats
        setStats({
          totalProducts: products.length,
          totalRetailers: retailers.length,
          totalPrices: prices.length
        })

        // Get recent prices (last 50)
        const sortedPrices = prices
          .sort((a, b) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime())
          .slice(0, 50)
        setRecentPrices(sortedPrices)
      } catch (error) {
        console.error('Failed to fetch dashboard data:', error)
      } finally {
        setLoading(false)
      }
    }

    fetchData()
  }, [])

  if (loading) {
    return (
      <div className="p-6">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {[...Array(3)].map((_, i) => (
            <Card key={i}>
              <CardHeader className="animate-pulse">
                <div className="h-4 bg-muted rounded w-3/4"></div>
                <div className="h-8 bg-muted rounded w-1/2"></div>
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
        <h1 className="text-3xl font-bold text-foreground">Dashboard</h1>
        <p className="text-muted-foreground">
          Monitor price trends across retailers
        </p>
      </div>

      {/* Stats Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Total Products</CardTitle>
            <Package className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{stats.totalProducts}</div>
            <p className="text-xs text-muted-foreground">
              Tracked across all retailers
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Retailers</CardTitle>
            <Store className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{stats.totalRetailers}</div>
            <p className="text-xs text-muted-foreground">
              Active retail partners
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Price Records</CardTitle>
            <TrendingUp className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{stats.totalPrices.toLocaleString()}</div>
            <p className="text-xs text-muted-foreground">
              Historical data points
            </p>
          </CardContent>
        </Card>
      </div>

      {/* Price Trends Chart */}
      <div className="grid grid-cols-1 lg:grid-cols-1 gap-6">
        <Card>
          <CardHeader>
            <CardTitle>Recent Price Trends</CardTitle>
            <CardDescription>
              Latest price movements across all products
            </CardDescription>
          </CardHeader>
          <CardContent>
            <PriceChart data={recentPrices} />
          </CardContent>
        </Card>
      </div>
    </div>
  )
}

