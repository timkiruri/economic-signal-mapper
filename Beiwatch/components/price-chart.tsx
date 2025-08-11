"use client"

import { Line, LineChart, XAxis, YAxis, CartesianGrid, ResponsiveContainer } from "recharts"
import { ChartContainer, ChartTooltip, ChartTooltipContent } from "@/components/ui/chart"
import { Price } from '@/lib/api'

interface PriceChartProps {
  data: Price[]
}

export function PriceChart({ data }: PriceChartProps) {
  // Transform data for chart
  const chartData = data
    .slice(0, 30) // Last 30 data points
    .map(price => ({
      date: new Date(price.timestamp).toLocaleDateString(),
      price: price.price,
      timestamp: price.timestamp
    }))
    .reverse() // Show chronologically

  return (
    <ChartContainer
      config={{
        price: {
          label: "Price (KES)",
          color: "hsl(var(--chart-1))",
        },
      }}
      className="h-[300px]"
    >
      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={chartData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis 
            dataKey="date" 
            fontSize={12}
            tickLine={false}
            axisLine={false}
          />
          <YAxis 
            fontSize={12}
            tickLine={false}
            axisLine={false}
            tickFormatter={(value) => `KES ${value}`}
          />
          <ChartTooltip content={<ChartTooltipContent />} />
          <Line 
            type="monotone" 
            dataKey="price" 
            stroke="var(--color-price)" 
            strokeWidth={2}
            dot={false}
          />
        </LineChart>
      </ResponsiveContainer>
    </ChartContainer>
  )
}
