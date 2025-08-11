import React from 'react';
import { Card, CardContent, Typography } from '@mui/material';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';

// Fix for default marker icons
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});

const RegionalMap = ({ regionalPrices, onRegionSelect }) => {
  const nairobiPosition = [-1.286389, 36.817223];

  return (
    <Card elevation={3}>
      <CardContent>
        <Typography variant="h6" gutterBottom>
          Regional Price Map
        </Typography>
        <div style={{ height: '400px', width: '100%' }}>
          <MapContainer 
            center={nairobiPosition} 
            zoom={7} 
            style={{ height: '100%', width: '100%' }}
          >
            <TileLayer
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
              attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            />
            
            {regionalPrices?.map((region) => (
              <Marker 
                key={region.id} 
                position={[region.lat, region.lng]}
                eventHandlers={{
                  click: () => onRegionSelect(region.id),
                }}
              >
                <Popup>
                  <div>
                    <strong>{region.name}</strong>
                    <p>Avg Price: KES {region.avgPrice.toFixed(2)}</p>
                  </div>
                </Popup>
              </Marker>
            ))}
          </MapContainer>
        </div>
      </CardContent>
    </Card>
  );
};

export default RegionalMap;