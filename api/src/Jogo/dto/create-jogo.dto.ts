import { ApiProperty, ApiPropertyOptional } from '@nestjs/swagger';
import {
  IsNotEmpty,
  IsNumber,
  IsOptional,
  IsString,
  MaxLength,
  Min,
} from 'class-validator';

export class CreateJogoDto {
  @ApiProperty({ example: 'Teclado mecânico' })
  @IsString()
  @IsNotEmpty()
  @MaxLength(120)
  nome: string;

  @ApiPropertyOptional({ example: 'Switch blue, layout ABNT2' })
  @IsOptional()
  @IsString()
  plan?: string;

  @ApiProperty()
  @IsNumber()
  @Min(0)
  start_date : date;
}